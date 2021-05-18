from pafy import new
while True:
    try:
        url = input("Enter URL: ")
        video = new(url)
        audio = new(url)
        video_quality = video.streams
        audio_quality = audio.audiostreams
        print("1- Information", "\n2- Download")
        num = int(input("Choose root number: "))

        if num == 1:
            print(new(url))
        elif num == 2:

            def quality(quality_type):
                number = 0
                for stream in quality_type:
                    number += 1
                    print(f"{number}- {stream}     size: {stream.get_filesize() / 1048576} MB")
                quality_number = int(input("Enter the quality number: "))
                filepath = input("Enter the file path: ")
                quality_type[quality_number - 1].download(filepath=filepath)

            print("1- Video", "\n2- Audio")
            Type = int(input("Choose root number: "))
            if Type == 1:
                quality(video_quality)
            elif Type == 2:
                quality(audio_quality)
            else:
                print("""Error!!
                                 (Wrong input)
                        Please, enter root correct input!""")
        else:
            print("""Error!!
                             (Wrong input)
                    Please, enter root correct input!""")
    except:
        print("""Error!!
                         (Wrong input)
                Please, enter root correct input!""")
