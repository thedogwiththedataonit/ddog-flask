from flask import Flask, render_template

#START VIRTUAL ENV in ZSH prompt 
# source env/bin/activate
# deactivate to stop virtual env


application = Flask(__name__)

@application.route('/')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    application.run(debug=True) #turn debug off for prodcution deployment

    