from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    #everytime we make changes our python file debug rerun the web server