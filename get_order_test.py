import sender_stand_request

# тест: проверить, что код ответа равен 200

def test_get_order_by_track_get_success_response():
    # в переменную track сохраняется результат запроса на получение номера заказа
    track = sender_stand_request.get_new_order_track()
    # в переменную response сохраняется результат запроса на получение заказа по его номеру
    response = sender_stand_request.get_order_by_track(track)
    # проверяем, что код ответа равен 200
    assert response.status_code == 200
