<script>
    import axios from "axios";
    import { onMount } from "svelte";
    import moment from 'moment';
    import Navbar from '../components/Navbar.svelte';



    let intervenants = [];

    onMount(async () => {
		await getIntervenants();
    });
    
    async function getIntervenants() {
        const res = await axios.get('http://127.0.0.1:5000/intervenants');
		intervenants = res.data;
    }
    
</script>

<style>
    .card-content {
        display: flex;
        justify-content: space-between;
        align-content: center;
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
<div class="card-content">
    {#each intervenants as intervenant}
        <div class="card" style="width: 18rem;">
            <img src={intervenant.url_photo} class="card-img-top" alt="photo">
            <div class="card-body">
                <h5 class="card-title">{intervenant.prenom} {intervenant.nom}</h5>
            </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item">{intervenant.mail}</li>
                <li class="list-group-item">{moment(intervenant.date_naissance).format('DD-MM-YYYY')}</li>
            </ul>
        </div>
    {/each}
</div>