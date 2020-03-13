<script>
  import { Router, Link, Route } from 'svelte-routing';
</script>

<style>
    .navbar {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .nav {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        width: 100%;
        background-color: black;
        margin-bottom: 2%;
    }

    li {
        margin-right: 5%;
        padding: 14px 25px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
    }

    a:visited {
        color: white !important;
        text-decoration: none !important;
    }

    a:hover {
        color: white ! important;
        text-decoration: none !important;
    }

</style>

<ul class="nav">
  <li class="nav-item">
    <Link to="/eleves">Élèves</Link>
  </li>
  <li class="nav-item">
    <Link to="/promotions">Promotions</Link>
  </li>
  <li class="nav-item">
    <Link to="/intervenants">Intervenants</Link>
  </li>
  <li class="nav-item">
    <Link to="/articles">Actualité</Link>
  </li>
</ul>