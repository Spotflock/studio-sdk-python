import studio


def main():
    c = studio.StudioClient('xxx')
    test_file_store_response = c.store('../csv/player_test.csv')
    print(test_file_store_response)
    test_data = test_file_store_response['fileUrl']
    train_data_store_response = c.store('../csv/player_train.csv')
    print(train_data_store_response)
    train_data = train_data_store_response['fileUrl']

    train_response = c.train("weka", "classification", "Player Churn Model", "NaiveBayesMultinomial",
                             train_data,
                             "player_activity", 80,
                             ["stamina", "challenges", "achievements"], True)
    print(train_response)
    train_job_status_response = c.job_status(train_response['data']['jobId'])
    print(train_job_status_response)
    train_job_output_response = c.job_output(train_response['data']['jobId'])
    print(train_job_output_response)
    model = train_job_output_response['output']['modelUrl']
    predict_response = c.predict("weka", "classification",
                                 test_data,
                                 model)
    print(predict_response)
    predict_job_status_response = c.job_status(predict_response['data'])
    print(predict_job_status_response)
    predict_job_output_response = c.job_output(predict_response['data'])
    print(predict_job_output_response)
    pred_file = predict_job_output_response['output']['predFileUrl']
    response = c.download(pred_file)
    print(response.text)


if __name__ == '__main__':
    main()


