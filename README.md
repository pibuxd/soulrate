<div class="head" align="center">
	<h3 align="center">
		<h1>Soulrate</h1>
	 </h3>
	<p align="center">
		<a href="https://pibux.pl" target="_blank">
			<img src="https://img.shields.io/website?down_color=critical&down_message=offline&logo=icloud&logoColor=ffffff&up_color=45966E&up_message=online&url=https%3A%2F%2Fpibux.pl" alt="website status" height="23">
		</a>
	</p>
	<h2></h2>
	<h3>
		<p align="center">
			<a href="./README.md#installation">[Installation]</a>
			&nbsp;
			<a href="./README.md#deployment">[Deployment]</a>
			&nbsp;
			<a href="./README.md#testing">[Testing]</a>
			&nbsp;
		</p>
	</h3>
	<h2></h2>
	<p>&nbsp;</p>
	<p align="center">
		<strong>
			Soulrate is a service where people evaluate each other.
			You can create an account and then start making the world great again.
		</strong>
	</p>
	<p>&nbsp;</p>
</div>

## Installation

Using pip

```sh
git clone github.com/pibuxd/soulrate
cd soulrate
python -m pip install -r ./requirements.txt
```
[Frontend installation and deployment](https://github.com/pibuxd/soulrate/blob/master/frontend/README.md)

## Deployment

```sh
gunicorn wsgi:app
```

## Testing

To run the whole API test suite

```sh
pytest
```

To run a specific test

```sh
pytest ./tests/{testname}
```
