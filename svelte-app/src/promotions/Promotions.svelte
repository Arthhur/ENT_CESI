<script>
    import axios from "axios";
    import { onMount } from "svelte";
    import moment from 'moment';
    import Navbar from '../components/Navbar.svelte';



    let promotions = [];

    onMount(async () => {
		await getPromotions();
    });
    
    async function getPromotions() {
        const res = await axios.get('http://127.0.0.1:5000/promotions');
		promotions = res.data;
    }
    
</script>

<Navbar />
<table class="table">
    <thead>
        <tr>
            <td>Nom</td>
            <td>Date début</td>
            <td>Date fin</td>
        </tr>     
    </thead>
    <tbody>
        {#each promotions as promotion}
        <tr>
            <td>{promotion.libelle}</td>
            <td>{moment(promotion.date_debut).format('DD-MM-YYYY')}</td>
            <td>{moment(promotion.date_fin).format('DD-MM-YYYY')}</td>
        </tr>
        {/each}
    </tbody>
</table>