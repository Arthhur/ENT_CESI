<script>
    import axios from "axios";
    import { navigate } from "svelte-routing";
    import {isAuth } from "../components/store/store"


    let username = '';
    let password = '';

    
	async function handleSubmit() {
        const data = {
            username,
            password
        }
        const res = await axios.post('http://127.0.0.1:5000/auth', data);
        if(res.data.length == 0) {
            console.log('bad');
        } 
        else {
            isAuth.set(true);
            navigate("/eleves", { replace: true });
        }
	}
</script>

<style>
    .auth-content {
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

<div class="auth-content">
    <div class="card" style="width: 18rem;">
        <h2>Authentification</h2>
        <div class="card-body">
            <input bind:value={username} type="text" placeholder="Your email">
            <input bind:value={password} type="password" placeholder="Your password">
        </div>
        <ul class="list-group list-group-flush">
                <button class="btn-connexion btn-primary" disabled={username == '' && password == ''} on:click={handleSubmit}>Login</button>
        </ul>
    </div>
</div>
