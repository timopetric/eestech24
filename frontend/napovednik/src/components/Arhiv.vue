<template>
    <div>
        <table>
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="row in csvData" :key="row.id">
                    <td>{{ row.date }}</td>
                    <td>{{ row.value }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import csv from 'csv-parser';
import fs from 'fs';

export default {
    data() {
        return {
            csvData: [],
        };
    },
    mounted() {
        fs.createReadStream('../data/vreme/processed/vreme_processed.csv')
            .pipe(csv())
            .on('data', (row) => {
                this.csvData.push(row);
            })
            .on('end', () => {
                console.log('CSV file successfully processed.');
            });
    },
};
</script>

<style>
/* Add your custom styles here */
</style>