#!/usr/bin/env python3
import os
import sys
import json


if __name__ == "__main__":
    SPACING = " " * 15

    original_file = "index.html"
    if not os.path.exists(original_file):
        print(f"ERROR: index.html not found")
        exit(1)

    original_content = open(original_file, "r").read()
    original_content_begin = original_content.split(f"{SPACING}<!-- SPEAKERS_START -->\n")[0]
    original_content_end = original_content.split(f"{SPACING}<!-- SPEAKERS_END -->\n")[1]

    speakers = json.loads(open("assets/speakers.json", "r").read())

    i = 0
    debug=False
    generated_code = ""

    if len(sys.argv) == 2 and sys.argv[1] == "debug":
        debug=True

    generated_code+=f"{SPACING}<!-- SPEAKERS_START -->\n"
    for name in speakers.keys():
        i += 1

        bio = speakers[name]['bio'].replace('\n', '</p><p>')
        picture = speakers[name]['picture'] 
        project = speakers[name]['project']
        
        image_path = f"./images/speakers/{picture}.jpg"
        if not os.path.exists(image_path):
            picture = "default"
            if debug:
                print(f"{image_path} not found")

        if debug:
            print(f"{name}")
            print(f"{image_path}")
            print(f"{picture}")

        generated_code += f"""{SPACING}<section id="speaker_{i}">
    {SPACING}<img class="circular-square" src="images/speakers/{picture}.jpg" alt="{name}"/>
    {SPACING}<h3>{name}</h3>
    {SPACING}<h4>{project}</h4>
    """

        if bio != "":
            generated_code += f"""
    {SPACING}<ul class="actions">
    {SPACING}    <li><a id="show_bio_{i}" onclick="showBio({i})" href="#speaker_{i}" class="button scrolly">Read Bio</a></li>
    {SPACING}</ul>
    {SPACING}<div id="bio_{i}" class="hidden">
    {SPACING}    <p>{bio}</p>
    {SPACING}    <ul class="actions">
    {SPACING}        <li><a id="hide_bio_{i}" onclick="hideBio({i})" href="#speaker_{i}" class="button scrolly">Hide Bio</a></li>
    {SPACING}    </ul>
    {SPACING}  </div>
    """

        generated_code += f"""
    {SPACING}</section>\n"""

    if i % 2 == 1:
        generated_code += f"{SPACING}<section></section>\n"

    generated_code+= f"{SPACING}<!-- SPEAKERS_END -->\n"

    new_content = f"{original_content_begin}{generated_code}{original_content_end}"
    new_content_file = open(original_file, "w")
    new_content_file.write(new_content)
    new_content_file.close()

