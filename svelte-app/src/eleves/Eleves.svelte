<script>
    import axios from "axios";
    import { onMount } from "svelte";
    import moment from 'moment';
    import Navbar from '../components/Navbar.svelte';
    import Articles from '../articles/Articles.svelte'


    let eleves = [];

    onMount(async () => {
		await getEleves();
    });
    
    async function getEleves() {
        const res = await axios.get('http://127.0.0.1:5000/eleves');
        eleves = res.data;
    }
    
</script>

<style>
    .eleve-content {
        display: flex;
        justify-content: flex-start;
        align-content: center;
        margin-bottom: 1%;
        width: 75%;
        height: 25rem;
        margin-right: 2%;
    }

    .container-eleve-blog {
        display: flex;
        justify-content: flex-start;
        width: 100%;
    }

    h5, .list-group-item {
        text-align: center;
    }

    .card-img-top {
        height: 200px;
    }

    .card-body {
        padding: 0.5rem;
    }
</style>

<Navbar />
<div class="container-eleve-blog">
    <div class="eleve-content">
        {#each eleves as eleve}
            <div class="card" style="width: 18rem;">
                <img src={eleve.url_image} class="card-img-top" alt="photo">
                <div class="card-body">
                    <h5 class="card-title">{eleve.prenom} {eleve.nom}</h5>
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">{eleve.mail}</li>
                    <li class="list-group-item">{moment(eleve.date_naissance).format('DD-MM-YYYY')}</li>
                    <li class="list-group-item">{eleve.libelle}</li>
                </ul>
            </div>
        {/each}
    </div>
    <Articles />
</div>


