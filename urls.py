def add_urls(app, sum_view):
    app.add_url_rule(
        "/sums/<string:task_id>/",
        view_func=sum_view.as_view("get_sums"),
        methods=["GET"]
    )
    app.add_url_rule(
        "/sums/<string:file>/",
        view_func=sum_view.as_view("calculate_sums"),
        methods=["POST"]
    )
