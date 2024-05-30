const sqlite3 = require('sqlite3').verbose();

const DB_DIR = process.env.DB_DIR;
const db = new sqlite3.Database(DB_DIR, (err: Error) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Connected to the mydb database.');
})

export function getListIndustriesFromDB() {
    return new Promise((resolve, reject) => {
        db.all('SELECT * FROM industries', (err: Error, rows: any) => {
            if (err) {
                console.error(err.message);
                reject(err);
            } else {
                resolve(rows);
            }
        });
    });
}
