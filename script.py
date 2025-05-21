from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip

def create_custom_video(input_video_path, output_video_path, text_line):
    # Load and resize the original video
    clip = VideoFileClip(input_video_path)
    clip = clip.resize(height=400)

    # Create white background (vertical, 720x1280)
    bg = ColorClip(size=(720, 1280), color=(255, 255, 255), duration=clip.duration)

    # Center the video clip on the background
    clip = clip.set_position(("center", "center"))

    # Add text above the video
    txt_clip = TextClip(text_line, fontsize=40, color='black', size=(700, None), font="Arial")
    txt_clip = txt_clip.set_position(("center", 100)).set_duration(clip.duration)

    # Composite all layers: background, video, and text
    final = CompositeVideoClip([bg, clip, txt_clip])

    # Export the final video
    final.write_videofile(output_video_path, fps=24)

# Example usage
if __name__ == "__main__":
    create_custom_video("input.mp4", "output.mp4", "This is your text above the video")
