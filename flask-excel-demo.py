from flask import Flask, make_response

app = Flask(__name__)


@app.route('/download')
def hello():
    output = make_response("demo.xlsx")
    output.headers["Content-Disposition"] = "attachment;filename=report.xlsx"
    output.headers["Content-type"] = "application/excel"
    return output


# @app.route("/")
# def main():
#     output = "hello world"
#     return output

if __name__ == '__main__':
    app.run()
