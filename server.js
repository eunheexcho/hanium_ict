import Express from "express";
import Mysql from "mysql";
import bodyParser from "body-parser";

const app = Express();

const mysqlConnection = Mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "acuous", // change the name
    multipleStatements: true
});

mysqlConnection.connect((err) => {
    if (err) {
        console.log('Connection failed :(');
        return;
    }
    console.log('Connected!! :)');
});

app.use(bodyParser.json());

app.get('/', function (req, res) {
    mysqlConnection.query("SELECT * from patient_info", (err, rows, field) => {
        if (!err) {
            res.send(rows)
        } else {
            console.log(err);
        }
    })
});

app.get('/patientinfo/:id', function (req, res) {
    mysqlConnection.query("SELECT * from patient_info WHERE rowid = ?", [req.params.id], (err, row) => {
        if (!err) {
            res.json(row)
        } else {
            console.log(err);
        }
    })
});

app.get('/urineinfo/:id', function (req, res) {
    mysqlConnection.query("SELECT u_info_id from patient_info", (err, rows, field) => {
        if (!err) {
            res.send(err)
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
