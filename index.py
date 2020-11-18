"""
from flask import Flask, render_template
from metricas import Metricas

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

metricas = Metricas()
print(metricas.detectarAnomalias())


@app.route('/', methods=("POST", "GET"))
def html_table():
    return render_template('anomalias.html',
                            tables=[metricas.detectarAnomalias().to_html(classes='dfanomalias', index=False)],
                            titles=metricas.df.columns.values)
"""