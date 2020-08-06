import Express from "express";
import Mysql from "mysql";
import bodyParser from "body-parser";

// const express = require("express");
// const mysql = require("mysql");
// const bodyParser = require("body-parser")

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
    console.log('Connected :)');
});

app.use(bodyParser.json());

app.get('/', function (req, res) {
    mysqlConnection.query("SELECT * from patientinfo", (err, rows, field) => {
        if (!err) {
            res.send(rows)
        } else {
            console.log(err);
        }
    })
});

app.get('/patientinfo/:id', function (req, res) {
    mysqlConnection.query("SELECT * from patientinfo WHERE rowid = ?", [req.params.id], (err, row) => {
        if (!err) {
            res.json(row)
        } else {
            console.log(err);
        }
    })
});

app.get('/urineinfo/:id', function (req, res) {
    mysqlConnection.query("SELECT urineinfo_id from patientinfo", (err, rows, field) => {
        if (!err) {
            res.send(err)
        } else {
            console.log(err);
        }
    })
});

app.post('/patientinfo', function (req, res) {
    mysqlConnection.query("INSERT INTO patientinfo VALUES (?, ?, ?, ?, ?)",
        [req.body.name, req.body.patientnum, req.body.age, req.body.sex, req.body.medicalDiagnosis], (err) => {
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
