import studio


def main():
    c = studio.StudioClient('xxx')

    response = c.face_detection_image('../img/fd-actual-img.jpg')  # it will return base-64 encoded image.
    print(response)
    response = c.face_detection_json('../img/fd-actual-img.jpg')  # it will return the co-ordinates of detected faces
    print(response)
    response = c.license_plate_detection_image('../img/lp-actual-img.jpg')  # it will return base-64 encoded image.
    print(response)
    response = c.license_plate_detection_json(
        '../img/lp-actual-img.jpg')  # it will return the co-ordinates of detected licence plates.
    print(response)


if __name__ == '__main__':
    main()
