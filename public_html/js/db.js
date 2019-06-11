const mysql = require('mysql');

var DB_option = {
  host     : 'db.dasom.io',
  user     : 'root',
  password : 'dasomDASOM',
  port     : 3306,
  database : 'dbdbdp'
};

console.log("연결 성공");

module.exports = mysql.createConnection(DB_option);
