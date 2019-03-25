import studio


def main():
    c = studio.StudioClient('xxx')
    response = c.sentiment_analysis('I am feeling good.')
    print(response)
    response = c.pos_tagger('I am Aniket.')
    print(response)


if __name__ == '__main__':
    main()
