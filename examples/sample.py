import studio


def main():
    c = studio.StudioClient('xxx')
    response = c.pos_tagger('I an Aniket.')
    print(response)
    response = c.sentiment_analysis('I am feeling good.')
    print(response)
    response = c.face_detection_image('../img/fd-actual-img.jpg')
    print(response)
    response = c.face_detection_json('../img/fd-actual-img.jpg')
    print(response)
    response = c.license_plate_detection_image('../img/lp-actual-img.jpg')
    print(response)
    response = c.license_plate_detection_json('../img/lp-actual-img.jpg')
    print(response)

    response = c.store('../csv/C2ImportCalEventSample.csv')
    print(response)
    response_1 = c.train("weka", "classification", "Player Churn Model", "NaiveBayesMultinomial",
                         "/spotflock-studio-prod/anurag@spotflock.com/1551256374428-player_train.csv",
                         "player_activity", 80,
                         ["stamina", "challenges", "achievements"], True)
    print(response_1)
    response = c.job_status(response_1['data']['jobId'])
    print(response)
    response = c.job_output(response_1['data']['jobId'])
    print(response)
    response_2 = c.predict("weka", "classification",
                           "/spotflock-studio-prod/anurag@spotflock.com/1551256370732-player_test.csv",
                           response['output']['modelUrl'])
    print(response_2)
    response = c.job_status(response_2['data'])
    print(response)
    response = c.job_output(response_2['data'])
    print(response)
    response = c.download('/spotflock-studio-prod/22/1551256606766-prediction.csv')
    print(response.text)

    response = c.train("weka", "regression", "Housing Price Model", "LinearRegression",
                       "/spotflock-studio-prod/anurag@spotflock.com/1551244089617-housing_test.csv", "price", 80,
                       ["area", "parking_area"], True)
    print(response)
    response = c.job_status(response['data']['jobId'])
    print(response)
    response = c.predict("weka", "regression", "/spotflock-studio/mounika/player_test.csv",
                         "/spotflock-studio/1/1550423221357-NaiveBayesMultinomial.mdl")
    print(response)
    response = c.cluster("He has been always cheerful ever since he moved to Hyderabad.")
    print(response)
    response = c.job_output(20)
    print(response)

    response = c.store('../csv/housing_test.csv')
    print(response)
    response = c.store('../csv/housing_train.csv')
    print(response)
    response = c.store('../csv/player_test.csv')
    print(response)
    response = c.store('../csv/player_train.csv')
    print(response)


if __name__ == '__main__':
    main()

