import services

def main():
    show_header()
    services.download_info()
    display_results()

def show_header():
    print("Welcome to Talk Python episode downloader")
    print()

def display_results():
    for show_id in range(120, 141):
        info = services.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))

if __name__ == '__main__':
    main()