<script>
    import axios from "axios";
    import { onMount } from "svelte";
    import Navbar from '../components/Navbar.svelte';
    import moment from 'moment';




    let articles = [];

    onMount(async () => {
		await getArticles();
    });
    
    async function getArticles() {
        const res = await axios.get('http://127.0.0.1:5000/blogs');
		articles = res.data;
    }
    
</script>

<style>
    .article-content {
        display: flex;
        flex-direction: column;
        align-content: center;
        margin-bottom: 0.5%;
    }

    h5, .list-group-item {
        text-align: center;
    }

    .card-img-top {
        height: 200px;
    }

    .card-body {
        padding: 0.5rem;
        background-color: black;
        color: white
    }

    .date, .categorie {
        background-color: black;
        color: white;
    }

    .card {
        margin-bottom: 0.5%;
    }
</style>

<div class="article-content">
{#each articles as article}
    <div class="card" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">{article.titre}</h5>
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item date">{moment(article.date_publication).format('DD-MM-YYYY')}</li>
            <li class="list-group-item">{article.contenu}</li>
            <li class="list-group-item categorie">{article.categorie}</li>
        </ul>
    </div>
{/each}
</div>
