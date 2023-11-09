/*
	Hyperspace by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$body = $('body'),
		$sidebar = $('#sidebar');

	// Breakpoints.
		breakpoints({
			xlarge:   [ '1281px',  '1680px' ],
			large:    [ '981px',   '1280px' ],
			medium:   [ '737px',   '980px'  ],
			small:    [ '481px',   '736px'  ],
			xsmall:   [ null,      '480px'  ]
		});

	// Hack: Enable IE flexbox workarounds.
		if (browser.name == 'ie')
			$body.addClass('is-ie');

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Forms.

		// Hack: Activate non-input submits.
			$('form').on('click', '.submit', function(event) {

				// Stop propagation, default.
					event.stopPropagation();
					event.preventDefault();

				// Submit form.
					$(this).parents('form').submit();

			});

	// Sidebar.
		if ($sidebar.length > 0) {

			var $sidebar_a = $sidebar.find('a');

			$sidebar_a
				.addClass('scrolly')
				.on('click', function() {

					var $this = $(this);

					// External link? Bail.
						if ($this.attr('href').charAt(0) != '#')
							return;

					// Deactivate all links.
						$sidebar_a.removeClass('active');

					// Activate link *and* lock it (so Scrollex doesn't try to activate other links as we're scrolling to this one's section).
						$this
							.addClass('active')
							.addClass('active-locked');

				})
				.each(function() {

					var	$this = $(this),
						id = $this.attr('href'),
						$section = $(id);

					// No section for this link? Bail.
						if ($section.length < 1)
							return;

					// Scrollex.
						$section.scrollex({
							mode: 'middle',
							top: '-20vh',
							bottom: '-20vh',
							initialize: function() {

								// Deactivate section.
									$section.addClass('inactive');

							},
							enter: function() {

								// Activate section.
									$section.removeClass('inactive');

								// No locked links? Deactivate all links and activate this section's one.
									if ($sidebar_a.filter('.active-locked').length == 0) {

										$sidebar_a.removeClass('active');
										$this.addClass('active');

									}

								// Otherwise, if this section's link is the one that's locked, unlock it.
									else if ($this.hasClass('active-locked'))
										$this.removeClass('active-locked');

							}
						});

				});

		}

	// Scrolly.
		$('.scrolly').scrolly({
			speed: 1000,
			offset: function() {

				// If <=large, >small, and sidebar is present, use its height as the offset.
					if (breakpoints.active('<=large')
					&&	!breakpoints.active('<=small')
					&&	$sidebar.length > 0)
						return $sidebar.height();

				return 0;

			}
		});

	// Spotlights.
		$('.spotlights > section')
			.scrollex({
				mode: 'middle',
				top: '-10vh',
				bottom: '-10vh',
				initialize: function() {

					// Deactivate section.
						$(this).addClass('inactive');

				},
				enter: function() {

					// Activate section.
						$(this).removeClass('inactive');

				}
			})
			.each(function() {

				var	$this = $(this),
					$image = $this.find('.image'),
					$img = $image.find('img'),
					x;

				// Assign image.
					$image.css('background-image', 'url(' + $img.attr('src') + ')');

				// Set background position.
					if (x = $img.data('position'))
						$image.css('background-position', x);

				// Hide <img>.
					$img.hide();

			});

	// Features.
		$('.features')
			.scrollex({
				mode: 'middle',
				top: '-20vh',
				bottom: '-20vh',
				initialize: function() {

					// Deactivate section.
						$(this).addClass('inactive');

				},
				enter: function() {

					// Activate section.
						$(this).removeClass('inactive');

				}
			});

})(jQuery);

function getIstanbulTime(input_date) {
  var local_time = input_date.toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }).split(" ");
  var am_pm = local_time[2];
  var result = local_time[1].split(":");
  result.pop();
  return result.join(":") + " " + am_pm;
}

function getNameIds() {
  var name_ids = {};
  $.ajax({
    'async': false,
    'global': false,
    'url': "/assets/speakers.json",
    'dataType': "json",
    'success': function (data) {
      name_ids = data;
    }
  });
  return name_ids;
}

function getSessionHtml(session, name_ids) {
  var session_id = session.id;
  var session_name = session.name;
  var session_description = session.description;
  var session_start_time = session.start;
  var session_end_time = session.end;
  var session_speakers = session.speakers;
  var session_speaker_names = [];
  var session_start = new Date(session_start_time);
  var session_end = new Date(session_end_time);
  for (var j = 0; j < session_speakers.length; j++) {
    var session_speaker = session_speakers[j];
    var session_speaker_name = session_speaker.name;
    session_speaker_names.push(session_speaker_name);
  }
  var session_speaker_names_string = session_speaker_names.join(", ");
  var session_start_time = getIstanbulTime(session_start);
  var session_end_time = getIstanbulTime(session_end);
  var times = session_start_time + " - " + session_end_time;
  var session_html = "<section id=\"session_" + session_id + "\"><h2>" + session_name + "</h2><h3>" + times + "</h3>"

  for (var j = 0; j < session_speakers.length; j++) {
    var session_speaker = session_speakers[j];
    var session_speaker_id = session_speaker.id;
    var session_speaker_name = session_speaker.name;

    // TODO: Remove this when API returns the correct name
    if (session_speaker_name == "Simi Vera") {
      session_speaker_name = "Smriti Verma";
      session_speaker_id = "smriti_verma";
      session_speaker_names_string = session_speaker_names_string.replace("Simi Vera", "Smriti Verma");
    }

    if (session_speaker_name in name_ids) {
      session_speaker_id = name_ids[session_speaker_name].picture;
    }
    session_html += "<img class=\"circular-square\" src=\"images/speakers/"+ session_speaker_id +".jpg\" alt=\"" + session_speaker_name + "\" />";
  }

  session_html += "<h4>" + session_speaker_names_string + "</h4>";
  session_html += "<ul class=\"actions\"><li><a id=\"show_desc_" + session_id + "\" onclick=\"showDescription('" + session_id + "')\" href=\"#session_" + session_id + "\" class=\"button scrolly\">Show Talk Description</a></li></ul>";
  session_html += "<p id=\"session_desc" + session_id + "\" class=\"hidden\">" + session_description + "</p>";
  session_html += "<ul class=\"actions\"><li><a id=\"hide_desc_" + session_id + "\" onclick=\"hideDescription('" + session_id + "')\" href=\"#session_" + session_id + "\" class=\"button scrolly hidden\">Hide Description</a></li></ul></section>";
  return session_html;
}

function loadSessions() {
  var name_ids = getNameIds();

  $.ajax({
    url: "https://app.streameth.org/api/organizations/devconnect/events/evm_summit/sessions?stage=emirgan_1"
  }).then(function(sessions) { // Main Stage
    $("#sessions-main").append("<h2>Emirgan 1</h2>");
    for (var i = 0; i < sessions.length; i++) {
      var session = sessions[i];
      session_html = getSessionHtml(session, name_ids);
      $("#sessions-main").append(session_html);
    }
  }).then(function () {
    $.ajax({
      url: "https://app.streameth.org/api/organizations/devconnect/events/evm_summit/sessions?stage=emirgan_2"
    }).then(function(sessions) { // Breakout Stage
      $("#sessions-breakout").append("<h2>Emirgan 2</h2>");
      for (var i = 0; i < sessions.length; i++) {
        var session = sessions[i];
        session_html = getSessionHtml(session, name_ids);
        $("#sessions-breakout").append(session_html);
      }
    }).then(function() {
      // Update scrolly.
      $('.scrolly').scrolly({
        speed: 1000,
        offset: function() {

          // If <=large, >small, and sidebar is present, use its height as the offset.
            if (breakpoints.active('<=large')
            &&	!breakpoints.active('<=small')
            &&	$sidebar.length > 0)
              return $sidebar.height();

          return 0;
        }
      });
    });
  });
}

function showSessions(room) {
  var main_stage = document.getElementById("sessions-main");
  var breakout_stage = document.getElementById("sessions-breakout");
  var main_room_button = document.getElementById("emirgan1-button");
  var breakout_room_button = document.getElementById("emirgan2-button");

  if (room == "emirgan1") {
    main_stage.style.display = "block";
    breakout_stage.style.display = "none";
    breakout_room_button.classList.remove("disabled");
    main_room_button.classList.add("disabled");
  } else {
    main_stage.style.display = "none";
    breakout_stage.style.display = "block";
    breakout_room_button.classList.add("disabled");
    main_room_button.classList.remove("disabled");
  }
}


function showMenu() {
  var x = document.getElementById("navLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

function showBio(bio_id) {
  var show_bio_link = document.getElementById("show_bio_" + bio_id);
  var bio = document.getElementById("bio_" + bio_id);

  show_bio_link.style.display = "none";
  bio.style.display = "block";
}

function hideBio(bio_id) {
  var show_bio_link = document.getElementById("show_bio_" + bio_id);
  var bio = document.getElementById("bio_" + bio_id);

  show_bio_link.style.display = "block";
  bio.style.display = "none";
}

function showDescription(session_id) {
  var show_desc_link = document.getElementById("show_desc_" + session_id);
  var hide_desc_link = document.getElementById("hide_desc_" + session_id);
  var desc = document.getElementById("session_desc" + session_id);

  show_desc_link.classList.add("hidden");
  hide_desc_link.classList.remove("hidden");
  desc.classList.remove("hidden");
}

function hideDescription(session_id) {
  var show_desc_link = document.getElementById("show_desc_" + session_id);
  var hide_desc_link = document.getElementById("hide_desc_" + session_id);
  var desc = document.getElementById("session_desc" + session_id);

  show_desc_link.classList.remove("hidden");
  hide_desc_link.classList.add("hidden");
  desc.classList.add("hidden");
}
