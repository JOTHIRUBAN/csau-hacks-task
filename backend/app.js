const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { Pool } = require('pg');

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(cors());

const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'postgres',
    password: 'postgres',
    port: 5432,
});

app.get('/expenses', async (req, res) => {
    try {
        const result = await pool.query('SELECT id, expense_name, expense_category, amount, TO_CHAR(expense_date, \'YYYY-MM-DD\') as expense_date FROM expenses');
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.post('/expenses', async (req, res) => {
    const { expense_name, expense_category, amount, expense_date } = req.body;
    try {
        const result = await pool.query(
            'INSERT INTO expenses (expense_name, expense_category, amount, expense_date) VALUES ($1, $2, $3, $4) RETURNING *',
            [expense_name, expense_category, amount, expense_date]
        );
        res.status(201).json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.put('/expenses/:id', async (req, res) => {
    const id = parseInt(req.params.id);
    const { expense_name, expense_category, amount, expense_date } = req.body;
    try {
        const result = await pool.query(
            'UPDATE expenses SET expense_name = $1, expense_category = $2, amount = $3, expense_date = $4, updated_at = CURRENT_TIMESTAMP WHERE id = $5 RETURNING *',
            [expense_name, expense_category, amount, expense_date, id]
        );
        res.json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.delete('/expenses/:id', async (req, res) => {
    const id = parseInt(req.params.id);
    try {
        await pool.query('DELETE FROM expenses WHERE id = $1', [id]);
        res.status(204).send();
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
