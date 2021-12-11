from backend.app import app_service


def main():
    app_service.run(debug=True)


if __name__ == '__main__':
    main()
