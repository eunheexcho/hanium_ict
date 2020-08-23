import Express from "express";
import Mysql from "mysql";
import bodyParser from "body-parser";
import helmet from "helmet";
import mysqlConnection from "./db.js";

const app = Express();

app.use(helmet());

app.use(bodyParser.json());

app.get('/', function (req, res) {
    mysqlConnection.query("SELECT * from patient_info", (err, rows) => {
        if (!err) {
            res.send(rows)
        } else {
            console.log(err);
        }
    })
});

app.get('/patientinfo/:id', function (req, res) {
    mysqlConnection.query("SELECT * from patient_info WHERE id = ?", [req.params.id], (err, rows) => {
        if (!err) {
            res.json(rows)
        } else {
            console.log(err);
        }
    })
});

app.get('/urineinfo/:id', function (req, res) {
    mysqlConnection.query("SELECT * from u_info WHERE id =?", [req.params.id], (err, rows) => {
        if (!err) {
            res.send(rows)
        } else {
            console.log(err);
        }
    })
});

app.post('/patientinfo', function (req, res) {
    mysqlConnection.query("INSERT INTO patient_info VALUES (?, ?, ?, ?, ?)",
        [req.body.name, req.body.patientnum, req.body.age, req.body.sex, req.body.meddx], (err) => {
            if (!err) {
                res.send()
            } else {
                console.log(err);
            }
        })
});

app.listen(3000, function () {
    console.log('Listening on Port 3000');
});
