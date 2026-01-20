<script>
    let articles = [];

    fetch("/data/data.json")
        .then(res => res.json())
        .then(json => {
            articles = json["Extracted datas"].data;
        });
</script>

<main>
    <header>
        <div class="logo-sct">
            <img src="logo.png" alt="Microsoft logo" class="logo-img" />
            <span class="logo-title">Microsoft Dev News</span>
        </div>

        <div class="contact">
            <button class="contact-btn"><a class="contact-a-btn" href="https://github.com/Thekorzeremi/DailyKorben">Aller sur le repo GitHub</a></button>
        </div>
    </header>

	<div class="source-label-sct">
		<span class="source-label">Korben</span>
	</div>
    <section class="articles">
        {#each articles as article}
            <article class="card">
				<img class="article-img" src={article.image} alt="news">
                <h2>{article.title}</h2>
                <p>{article.content}</p>
				<p class="source">Source : Korben</p>
            </article>
        {/each}
    </section>
</main>

<style>
	* {
		overflow: hidden;
	}

    main {
        width: 100%;
        min-height: 100vh;
        background: #f3f3f5;
        font-family: "Segoe UI", sans-serif;
        color: #1b1b1b;
    }

    header {
        height: 70px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #ffffffcc;
        backdrop-filter: blur(12px);
        border-bottom: 1px solid #e1e1e1;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }

	.source-label-sct {
		margin-left: 20px;
		margin-top: 20px;
		width: max-content;
		background: #ffffff;
        padding: 10px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
	}

	.source-label {
		font-size: x-large;
		font-weight: 400;
	}

    .logo-sct {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-left: 15px;
    }

    .logo-img {
        height: 45px;
        width: 45px;
        border-radius: 10%;
        background: white;
        padding: 4px;
    }

    .logo-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #323130;
    }

    .contact {
        margin-right: 15px;
    }

    .contact-btn {
        background-color: #5b5fc7;
        color: white;
        border: none;
        padding: 8px 14px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 0.9rem;
        transition: background 0.2s;
    }

    .contact-btn:hover {
        background-color: #4a4fb5;
    }

	.contact-a-btn {
		color: white;
	}

    .articles {
        padding: 20px;
        display: grid;
        gap: 20px;
        grid-template-columns: 1fr;
    }

	.article-img {
		height: auto;
		width: 100%;
		margin-bottom: 2.5%;
	}

    @media (min-width: 700px) {
        .articles {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (min-width: 1100px) {
        .articles {
            grid-template-columns: repeat(3, 1fr);
        }
    }

    .card {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
		cursor: pointer;
    }

    .card h2 {
        margin: 0 0 10px 0;
        font-size: 1.2rem;
        color: #201f1e;
    }

    .card p {
        margin: 0;
        line-height: 1.45;
        color: #3b3a39;
    }
</style>