from flask import Flask, render_template, redirect
from application import *

app = Flask(__name__)

@app.route("/")
def loginform():
    return render_template("LOGINFORM.html")

@app.route("/login", methods = ["POST"])
def login():
    return redirect('home.html')

@app.route("/home.html")
def home():
    port_analysis_time = run_port_analysis()[0][0]
    arp_analysis_time = run_arp_analysis()[0][0]
    syn_analysis_time = run_syn_analysis()[0][0]
    return render_template("home.html",
                           port_analysis_time=port_analysis_time,
                           arp_analysis_time=arp_analysis_time,
                           syn_analysis_time=syn_analysis_time)

@app.route("/detailsarp.html")
def detailsarp():
    analysis = run_arp_analysis()
    return render_template("detailsarp.html", analysis=analysis)

@app.route("/detailsportscanning.html")
def detailsportscanning():
    analysis = run_port_analysis()
    return render_template("detailsportscanning.html", analysis=analysis)

@app.route("/detailssynflood.html")
def detailssynflood():
    analysis = run_syn_analysis()
    return render_template("detailssynflood.html", analysis=analysis)

@app.route("/HELPsyn.html")
def helpsyn():
    return render_template("HELPsyn.html")

@app.route("/HELParp.html")
def helparp():
    return render_template("HELParp.html")

@app.route("/HELPport.html")
def helpport():
    return render_template("HELPport.html")

if __name__ == "__main__":
    app.run(debug=True)