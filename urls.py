def add_urls(app, sum_view, count_view):
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

    app.add_url_rule(
        "/count/",
        view_func=count_view.as_view("get_count"),
        methods=["GET"]
    )
