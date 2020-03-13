<script>
	import Eleves from './eleves/Eleves.svelte';
	import Intervenants from './intervenants/Intervenants.svelte';
	import Promotions from './promotions/Promotions.svelte';
	import Articles from './articles/Articles.svelte';
	import AddArticle from './articles/AddArticle.svelte';
	import EmploiDuTemps from './emploidutemps/EmploiDuTemps.svelte';
	import Header from './components/Header.svelte';
	import Navbar from './components/Navbar.svelte';
	import Redirect from './components/Redirect.svelte';
	import PageNotFound from './components/PageNotFound.svelte';
	import Authentification from './authentification/authentification.svelte'
	import { Router, Link, Route } from 'svelte-routing';
	import axios from "axios";
	//import { isAuth } from './store';



	export let url = '';
	let auth = false;
	/*const unsubscribe = isAuth.subscribe(value => {
		auth = value;
	});*/

</script>

<svelte:head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
</svelte:head>

<Header />
<div class="section columns">
  <Router {url}>
    <main class="column">
      <div>
        <Route path="/" component={Authentification} />
        <Route path="/eleves" component={Eleves} />
		<Route path="/articles" component={AddArticle} />
        <Route path="/promotions" component={Promotions} />
        <Route path="/blogs" component={Articles} />
		<Route path="/intervenants" component={Intervenants} />
		<Route path="/emploi-temps" component={EmploiDuTemps} />
        <Route path="**" component={PageNotFound} />
      </div>
    </main>
  </Router>
</div>