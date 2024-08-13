def parse_srt(filename):
    """
    Parses a subtitle file in .srt format and returns a dictionary of subtitles.

    Args:
        filename: The path to the .srt file.

    Returns:
        A dictionary where each key is a subtitle ID and the value is a dictionary
        with the following keys:
        "ID": The subtitle ID (integer).
        "start-time": The subtitle start time (string in hh:mm:ss,mmm format).
        "end-time": The subtitle end time (string in hh:mm:ss,mmm format).
        "sentence": The subtitle text (string).
    """
    subtitles = {}
    current_id = None
    current_text = []

    with open(filename, 'r', encoding='utf-8-sig') as file:
        for line in file:
            line = line.strip()
            if line.isdigit():
            # New subtitle block
                current_id = int(line)
                current_text = []
            elif line and ' --> ' in line:
            # Start/end time
                start_time, end_time = line.split(' --> ')
            elif line:
            # Subtitle text
                current_text.append(line)
            else:
            # Empty line, finalize subtitle
                if current_id and current_text:
                    subtitles[current_id] = {
                    "ID": current_id,
                    "start_time": start_time,
                    "end_time": end_time,
                    "sentence": "\n".join(current_text),
                    }
                current_id = None

    return subtitles
    # Example usage
    #filename = "Saving.Private.Ryan.srt"
    #subtitle_dict = parse_srt(filename)
    # for keys in subtitle_dict:
    #     print(subtitle_dict[keys]['start-time'])

def create_srt(subtitle_dict, filename):
    """
    Creates a subtitle file in .srt format from a dictionary of subtitles.

    Args:
        subtitle_dict: A dictionary where each key is a subtitle ID and the value is a dictionary
                        with the following keys:
                            "ID": The subtitle ID (integer).
                            "start-time": The subtitle start time (string in hh:mm:ss,mmm format).
                            "end-time": The subtitle end time (string in hh:mm:ss,mmm format).
                            "sentence": The subtitle text (string).
        filename: The path to the output .srt file.
    """

    with open(filename, 'w', encoding='utf-8-sig') as file:
        for subtitle_id, subtitle in subtitle_dict.items():
            file.write(f"{subtitle_id}\n")
            file.write(f"{subtitle['start_time']} --> {subtitle['end_time']}\n")
            file.write(f"{subtitle['sentence']}\n\n")
        # file.write(f"{subtitle['translate']}\n\n")

    # Example usage
    # subtitle_dict = {
    #     1: {
    #         "ID": 1,
    #         "start-time": "00:00:10.000",
    #         "end-time": "00:00:20.000",
    #         "sentence": "This is the first subtitle.",
    #     },
    #     2: {
    #         "ID": 2,
    #         "start-time": "00:00:30.000",
    #         "end-time": "00:00:40.000",
    #         "sentence": "This is the second subtitle.",
    #     },
    # }
    # create_srt(subtitle_dict, "output_subtitles.srt")