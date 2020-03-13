<script>
    import { onMount } from "svelte";
    import { navigate } from "svelte-routing";
    import {isAuth } from "../components/store/store"
    let auth = false;

    onMount( () => {
		const unsubscribe = isAuth.subscribe(value => {
            auth = value;
	    });
    });

	function deconnexion() {
        isAuth.set(false);
        navigate("/", { replace: true });
    }
    
</script>

<style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }

    .logo-cesi {
        width: 20rem;
    }

    h1 {
        margin-right: 20%;
    }

    .btn-invisible {
        visibility: hidden;
    }

</style>


<div class="header-container">
    <img class="logo-cesi" src="images/Cesi-logo.jpg" alt="cesi-logo" />
    <h1>ENT CESI</h1>
    {#if auth}
        <button type="button" class="btn btn-dark" on:click={deconnexion}>Déconnexion</button>
    {:else}
        <button class="btn-invisible"></button>
    {/if}
</div>