import services


def main():
    print("Welcome to Talk Python episode downloader")
    print()

    services.download_info()

    # TODO: print all episode title
    for show_id in range(100, 130):
        info = services.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))

if __name__ == '__main__':
    main()
