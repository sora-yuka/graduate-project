<template>
    <nav class="nav">
        <div class="container">
            <router-link to="/"><span class="home-button">COURSERA</span></router-link>
            <ul class="nav-bar">
                <!-- <li class="nav-bar__item"><router-link to="/about" class="router-link">about</router-link></li> -->
                <ul class="sign-in">
                    <li class="sign-in__item"><router-link to="/login" class="sign-in__button">Log In</router-link></li>
                    <li class="sign-in__item"><router-link to="/register" class="sign-in__button">Register</router-link></li>
                </ul>
            </ul>
        </div>
    </nav>
    <router-view/>
</template>

<style>
@import './components/css/main.css';

</style>