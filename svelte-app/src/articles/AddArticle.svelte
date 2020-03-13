<script>
    import axios from "axios";
    import Navbar from '../components/Navbar.svelte';
    import { navigate } from "svelte-routing";
    import moment from 'moment';




    let titre = '';
    let contenu = '';
    let categorie = '';

    async function submit() {
        const date_publication = moment(new Date()).format('YYYY-MM-DD');
        const data = {
            titre,
            contenu,
            categorie,
            date_publication,
            id_categorie: 1
        };
        const res = await axios.post('http://127.0.0.1:5000/blogs', data);
        res.data.length == 0 ? console.log('bad') : navigate("/eleves", { replace: true });
    }
    
</script>

<style>
    .ajout-content {
        display: flex;
        width: 100%;
        justify-content: center;
    }

    input {
        margin-bottom: 5%;
    }

    h2 {
        text-align: center;
        padding: 1rem;
    }

    .card-body {
        text-align: center;
    }

    .btn-connexion:disabled {
        background-color: grey;
        border: none;
    }
</style>

<div class="ajout-content">
    <div class="card" style="width: 18rem;">
        <h2>Ajouter un article</h2>
        <div class="card-body">
            <input bind:value={titre} type="text" placeholder="titre">
            <input bind:value={contenu} type="text" placeholder="contenu">
            <input bind:value={categorie} type="text" placeholder="categorie">
        </div>
        <ul class="list-group list-group-flush">
            <button class="btn-connexion btn-primary" disabled={titre == '' && contenu == '' && categorie == ''} on:click={submit}>Ajouter</button>
        </ul>
    </div>
</div>
