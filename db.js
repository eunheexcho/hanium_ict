import Mysql from "mysql";

const mysqlConnection = Mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "******",
    database: "******",
    multipleStatements: true
});

mysqlConnection.connect((err) => {
    if (err) {
        console.log('Connection failed :(');
        return;
    }
    console.log('Connected!! :)');
});

// module.exports = {mysqlConnection};
export default mysqlConnection;
