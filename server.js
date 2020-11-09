import Express from "express";
import bodyParser from "body-parser";
import helmet from "helmet";
import mysqlConnection from "./db.js";

const app = Express();

app.use(helmet());

app.use(bodyParser.json());

app.get('/', function (req, res) {
    mysqlConnection.query("SELECT * from patients", (err, rows) => {
        if (!err) {
            res.send(rows)
        } else {
            console.log(err);
        }
    })
});

app.get('/patientinfo/:id', function (req, res) {
    mysqlConnection.query("SELECT * from patients WHERE id = ?", [req.params.id], (err, rows) => {
        if (!err) {
            res.json(rows)
        } else {
            console.log(err);
        }
    })
});

app.get('/urineinfo/:id', function (req, res) {
    mysqlConnection.query("SELECT * from urine_information WHERE id =?", [req.params.id], (err, rows) => {
        if (!err) {
            res.send(rows)
        } else {
            console.log(err);
        }
    })
});

// app.get('/alysisinfo', function (req, res) {
//     mysqlConnection.query("SELECT * from urinalysis_information WHERE id =?"), [req.parans.id], (err, rows) => {
//         if(!err) {
//             res.send(rows)
//         } else {
//             console.log(err);
//         }
//     }
// });

app.post('/patientinfo', function (req, res) {
    mysqlConnection.query("INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?)",
        [req.body.name, req.body.patient_number, req.body.age, req.body.sex, req.body.medical_diagnosis], (err) => {
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
