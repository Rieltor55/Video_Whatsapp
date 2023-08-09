from moviepy.editor import VideoFileClip

# Путь к исходному видео
video_path = "path"

# Путь для сохранения конвертированного видео
output_path = "path"

# Загружаем видео
video = VideoFileClip(video_path)

# Получаем длительность видео в секундах
duration = video.duration

# Изменяем размер видео
video_resized = video.resize(height=640)

# Сохраняем конвертированное видео
video_resized.write_videofile(output_path, codec="libx264", audio_codec="aac")
