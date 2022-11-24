html_content = '''
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>✨Python WebAPI Dev✨ - JIANG</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	text-indent: -1.7em;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
	empty-cells: show;
}
.simple-table td {
	height: 29px;
	min-width: 120px;
}

.simple-table th {
	height: 29px;
	min-width: 120px;
}

.simple-table-header-color {
	background: rgb(247, 246, 243);
	color: black;
}
.simple-table-header {
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-opaquegray { background-color: rgba(255, 255, 255, 0.0375); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="29f8d434-7ef9-4ee8-b902-c8e527b3f876" class="page sans"><header><img class="page-cover-image" src="https://images.unsplash.com/photo-1606787366850-de6330128bfc?ixlib=rb-4.0.3&amp;q=80&amp;fm=jpg&amp;crop=entropy&amp;cs=tinysrgb" style="object-position:center 50%"/><div class="page-header-icon page-header-icon-with-cover"><span class="icon">🐍</span></div><h1 class="page-title">✨Python WebAPI Dev✨ - JIANG</h1></header><div class="page-body"><h2 id="d8e314f1-3c85-4482-8952-3bfc746f00bf" class="">🖱️ Click below to navigate to the backend FastAPI page</h2><figure id="97aa71a7-85eb-4aea-b742-8e10344049cc"><a href="https://fastapi-jiang.herokuapp.com/docs" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">FastAPI - Swagger UI</div></div><div class="bookmark-href"><img src="https://fastapi.tiangolo.com/img/favicon.png" class="icon bookmark-icon"/>https://fastapi-jiang.herokuapp.com/docs</div></div></a></figure><hr id="130c3f7b-7c8b-4399-ade7-dcb76c598240"/><h2 id="956b3a04-045f-46cb-b05e-964eee47f856" class="">📚 Tech Stack</h2><ul id="6c88e6fb-e6bc-479f-a8dc-b141fa0d1dd1" class="bulleted-list"><li style="list-style-type:disc">Python<ul id="27b2e161-bf36-468a-84c6-2f5e96acd845" class="bulleted-list"><li style="list-style-type:circle"><strong>FastAPI</strong> (fastest API builder, Faster than Django and Flask)</li></ul><ul id="00066c36-c45a-4c42-b22d-888c742750ae" class="bulleted-list"><li style="list-style-type:circle"><strong>Sqlalchemy</strong> (SQL toolkit and relational mapper)</li></ul><ul id="a707bd4c-cdad-4af6-94e3-a63122fd00ac" class="bulleted-list"><li style="list-style-type:circle"><strong>Alembic</strong> (Database migration)</li></ul><ul id="a863e126-1b31-49fb-abdb-f77581ae743c" class="bulleted-list"><li style="list-style-type:circle"><strong>Pydantic</strong> (Modeling, data typing)</li></ul><ul id="849186e6-ac00-4ad9-af09-d4c39c9aa539" class="bulleted-list"><li style="list-style-type:circle"><strong>OAuth2</strong> (Authentication with Bear token)</li></ul><ul id="836b609e-61c4-4d44-ae82-4ae426b4a185" class="bulleted-list"><li style="list-style-type:circle">Psycopg2 (Database driver)</li></ul><ul id="1601e1a1-a36f-4335-a4ad-0d69c146b83b" class="bulleted-list"><li style="list-style-type:circle">Jose (Authentication with JSON Web Signature)</li></ul><ul id="26083fa0-c5ed-4ea6-947e-2fca46a40cc5" class="bulleted-list"><li style="list-style-type:circle">Passlib (SHA256 hash encryption for security)</li></ul><ul id="7ad1d52a-0175-4df8-86d8-43960f4efb59" class="bulleted-list"><li style="list-style-type:circle">Uvicorn (Local web server for testing)</li></ul></li></ul><ul id="66343df6-a201-4564-9a4c-2d3975c1eec5" class="bulleted-list"><li style="list-style-type:disc"><strong>PostgreSQL</strong> - free open-source relational database software</li></ul><ul id="a382f66c-7d47-45e1-a2b8-18fa11579c18" class="bulleted-list"><li style="list-style-type:disc">PgAdmin4 - GUI for PostgreSQL</li></ul><ul id="78b4b3f2-754b-4542-98c4-e3db9a1f9110" class="bulleted-list"><li style="list-style-type:disc"><strong>Postman</strong> - API testing</li></ul><ul id="0e1a04b1-5578-4a3f-a823-581f1c7c828c" class="bulleted-list"><li style="list-style-type:disc"><strong>Heroku</strong> - Web server host</li></ul><hr id="0e5a1628-425a-4e84-a9c3-bb18d7e72881"/><h2 id="f2693695-82a5-4cca-a508-e4973ae936ae" class="">☘️ API Details</h2><h3 id="399ab54c-ab10-48d0-a30b-52080647671b" class="">🏞️ Prerequisite</h3><p id="99ae9ff9-57ca-4a33-9dba-e3b910723d6c" class="">Firstly, <strong>create a user</strong> with Users ⇒ <code>Post</code> /users/ create user (green button) ⇒ <code>Try it out</code> =&gt; Edit &quot;email&quot; and &quot;password&quot; strings =&gt; <code>Execute</code>. In Server Response under the Responses section, if you see the 201 code with your account detail, congrats!</p><p id="c5b988e2-7f33-4197-b48e-bcf5f1051040" class="">Secondly, <strong>log in</strong> with <code>Authorize</code> (top right) button. You need to create a user first, following the instruction above.</p><p id="454f50c8-03f3-40fc-8094-a680077b0739" class="">Thirdly, you are now a freeman who can <strong>try some APIs</strong>.</p><h3 id="f7611c6f-960e-43f6-afb4-8ce7b52ecf73" class="">🎆 Posts</h3><ul id="52e3d560-2819-4ab7-b262-4e25b67ef64d" class="bulleted-list"><li style="list-style-type:disc">GET /posts/ - No specific authentication is needed. Expecting return of all created posts by all users</li></ul><ul id="33f15e73-5792-4b70-8689-1eca5bd7fe91" class="bulleted-list"><li style="list-style-type:disc">POST /posts/ - Expecting: 201 Code, in the Server response section</li></ul><ul id="55bf6243-0185-4fa4-8e99-6458b26215ca" class="bulleted-list"><li style="list-style-type:disc">POST /posts/ - Expecting: 201 Code, in the Server response section. Both time and your id would automatically logged in the backend</li></ul><ul id="eec2335a-a368-4390-a5da-2a8e5aa4ca62" class="bulleted-list"><li style="list-style-type:disc">PUT /posts/{id} - Expecting: 200 Code, in the Server response section. Your new post title and content would be updated</li></ul><ul id="8e5026ba-15dc-45ad-a272-89e01ac8ba3f" class="bulleted-list"><li style="list-style-type:disc">DELETE /posts/{id} - Expecting: 204 Code, in the Server response section. Your selected post would be deleted. Your login is required and you are only authorized to delete your own posts</li></ul><h3 id="48173ded-7f0f-4e11-98e6-10fe60a7c92e" class="">💁‍♂️ Users</h3><ul id="d184f559-78e4-4f1c-9a33-23b66047a0ab" class="bulleted-list"><li style="list-style-type:disc">POST /users/ - Expecting: 201 Code, in the Server response section. You will be assigned  a user id</li></ul><ul id="ad3f143a-ad82-4113-af2a-e314fefca1fa" class="bulleted-list"><li style="list-style-type:disc">GET /users/{id} - Expecting: 202 Code,  in the Server response section. It will return your account information</li></ul><h3 id="47a4b263-18bc-4a9b-9b3b-0b9d3d678e40" class="">🔐 Authentication</h3><ul id="d329b878-e51b-4afe-a9ec-cd4b9a923d94" class="bulleted-list"><li style="list-style-type:disc">POST /login - Expecting: 200 Code</li></ul><h3 id="2548ed44-36d7-4f18-a4c8-d899f084b7e7" class="">👍 Vote</h3><ul id="b0a92121-083d-4684-a65e-72a223c81152" class="bulleted-list"><li style="list-style-type:disc">POST /vote/ - Expecting: 200 Code with a success message. <code>post_id</code> is the post you want to vote on. <code>dir</code> is the direction of the vote: 1 is upvote, -1 is downvote. If you voted for this post id before, you can’t repeatedly upvote. The same as a downvote</li></ul><h3 id="c362da65-f704-441e-ae0f-f3798bbeffdd" class="">🍊 Default</h3><ul id="182cfad0-0ada-4618-9a26-37548f14e761" class="bulleted-list"><li style="list-style-type:disc">This route should you the current page of instructions and docs</li></ul><hr id="2451c103-e891-4bc5-b49e-a7b499fe9022"/><p id="d8d230d1-a8ac-4260-a0ac-5ec7ad5f5f1b" class="">
</p><h2 id="4e68be55-5da7-4f79-b0bb-020624c3ae46" class="">🍹 Project Reflection</h2><ol type="1" id="78667a9b-2f0c-48b8-a943-f476b9ae6342" class="numbered-list" start="1"><li>I am familiar with Conda environment and VS Code. I tried something new. Venv and PyCharm make a great combination, if you mind the biggest memory hog - PyCharm.</li></ol><ol type="1" id="d85b6372-a868-4d4f-9f80-faa90d309662" class="numbered-list" start="2"><li>Pydantic ensures data model. It is especially important because API building is basically building a data pipeline that ensures the data transform into the right format.</li></ol><ol type="1" id="f7a40859-6944-444d-b4f7-816436967387" class="numbered-list" start="3"><li>Data migration with scripting using Sqlalchemy and Alembic amazes me. Though I spent 1 whole day debugging Alembic version issue. However, it is worthy because it helps you implement all data schemes into a web server like Heroku very smoothly with the command <code>heroku run &quot;alembic upgrade head&quot;</code>.</li></ol><ol type="1" id="8196ae9f-ddb9-4a2e-b334-ff0bade829f0" class="numbered-list" start="4"><li>Create users, user login, user does CRUD operation on posts with authentication feature could be operated directly with <code>/docs</code>s or <code>/redoc</code> is very convenient. You don’t need Postman and you can test in a smaller scale. But nothing beats Postman’s environment features (DEV, PROD, Variable for secret tokens).</li></ol><hr id="5d6cb4b7-4dc8-45fa-acdd-5fd1c58bf5d4"/><h2 id="4ee4e8ec-e63b-41a0-abc1-c34e096ba20a" class="">⛓️ Links</h2><ul id="9fc51ede-2f67-4959-b434-750b5e7c3e92" class="bulleted-list"><li style="list-style-type:disc"><strong>Github page</strong><figure id="12054ee4-f577-4543-8233-2024f58291dd"><a href="https://github.com/zjian107-su" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">zjian107-su - Overview</div><div class="bookmark-description">You can&#x27;t perform that action at this time. You signed in with another tab or window. You signed out in another tab or window. Reload to refresh your session. Reload to refresh your session.</div></div><div class="bookmark-href"><img src="https://github.com/favicon.ico" class="icon bookmark-icon"/>https://github.com/zjian107-su</div></div><img src="https://avatars.githubusercontent.com/u/35544956?v=4?s=400" class="bookmark-image"/></a></figure></li></ul><ul id="7be04190-f109-4ee0-bce5-4f54e37f780d" class="bulleted-list"><li style="list-style-type:disc"><strong>Repository page</strong>: <a href="https://github.com/zjian107-su/Python-WebAPI-Dev">https://github.com/zjian107-su/Python-WebAPI-Dev</a></li></ul><ul id="6f434e35-c11a-49d0-81d3-7d58309c42c0" class="bulleted-list"><li style="list-style-type:disc"><strong>LinkedIn</strong><figure id="8076ffcd-2522-46c4-8ac6-728c234d7a18"><a href="https://www.linkedin.com/in/zezhengjiang/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title"></div></div><div class="bookmark-href">https://www.linkedin.com/in/zezhengjiang/</div></div></a></figure></li></ul><ul id="b35a1ec8-fecb-4aa5-9a4a-916891eb3d12" class="bulleted-list"><li style="list-style-type:disc"><strong>LeetCode</strong><figure id="e5001084-92f6-46d4-8f87-9092d9b69c84"><a href="https://leetcode.com/zjian107-su/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">zjian107-su - LeetCode Profile</div><div class="bookmark-description">View zjian107-su&#x27;s profile on LeetCode, the world&#x27;s largest programming community.</div></div><div class="bookmark-href"><img src="https://leetcode.com/favicon.ico" class="icon bookmark-icon"/>https://leetcode.com/zjian107-su/</div></div><img src="https://leetcode.com/static/images/LeetCode_Sharing.png" class="bookmark-image"/></a></figure></li></ul><ul id="7e2da981-84d7-46a0-944f-be2930c412bd" class="bulleted-list"><li style="list-style-type:disc"><strong>Syracuse University article about me</strong><figure id="556dc64c-a9cf-4f48-b910-21dd631264c0"><a href="https://www.syracuse.edu/stories/student-spring-break-silicon-valley-2019/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">A Transformative Trip to Silicon Valley - Syracuse.edu</div><div class="bookmark-description">What impressed Zezheng (Daniel) Jiang most about the wide range of companies the Syracuse student group visited during Spring Break in Silicon Valley (SBinSV) were the two attributes they all had in common-their diversity and enthusiasm. The entrepreneurs and employees came from all over the world and had varied academic backgrounds.</div></div><div class="bookmark-href"><img src="https://www.syracuse.edu/assets-static/img/favicons/favicon-192.png" class="icon bookmark-icon"/>https://www.syracuse.edu/stories/student-spring-break-silicon-valley-2019/</div></div><img src="https://www.syracuse.edu/images/Bp0-3i1YlGQHeC98Ybx_wjHHFfo=/3617/width-1100/daniel-v2-e1554473528208-1100x733_08-02-202117-31-28.jpg" class="bookmark-image"/></a></figure></li></ul><ul id="4ba1433a-edbf-4a34-a090-f6d21f8db93b" class="bulleted-list"><li style="list-style-type:disc"><strong>Newspaper (The Daily Orange) article about me</strong><figure id="ab8cc134-76bd-4aae-a193-2b51f6ae9c01"><a href="https://dailyorange.com/2015/10/qa-freshman-free-line-skater-talks-alternative-transportation/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Q&amp;A: Freshman free-line skater talks alternative transportation - The Daily Orange</div><div class="bookmark-description">Freshman Daniel Jiang turns heads when going from place to place on campus. His free-line skates - two platforms, one for each foot, with no straps to secure them on his feet - provide him with an unusual method of transportation.</div></div><div class="bookmark-href"><img src="https://dailyorange.com/favicon.ico" class="icon bookmark-icon"/>https://dailyorange.com/2015/10/qa-freshman-free-line-skater-talks-alternative-transportation/</div></div><img src="https://dailyorange.com/resize/220x180/wp-content/uploads/2022/11/16235545/CourtesyofWallyGobetz.jpg" class="bookmark-image"/></a></figure></li></ul><ul id="20895209-dcb2-4014-9995-c08d0ea73c92" class="bulleted-list"><li style="list-style-type:disc"><strong>My other web projects</strong><figure id="264378ae-c7c1-4608-889f-e6d8d923e311"><a href="https://nabi.io/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Home</div><div class="bookmark-description">The only stop to train a beautifully healthy and obedient dog</div></div><div class="bookmark-href"><img src="https://nabi.io/favicon-32x32.png?v=ae73c410a743cccd534e98d0bf000528" class="icon bookmark-icon"/>https://nabi.io/</div></div><img src="https://nabi.io/static/35a423b01a786d14f6d423b2082bb99f/630fb/gatsby-astronaut.png" class="bookmark-image"/></a></figure><figure id="190ac2dd-f66c-4b59-9a0d-5387f859d331"><a href="https://danielzezhengjiang.com/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">WebDev Portfolio</div><div class="bookmark-description">web development Web content development, client-side/server-side scripting. Using React and Django web design Planning, building architecture, arranging content. Using HTML, CSS app design User interface (UI) and user experience (UX).</div></div><div class="bookmark-href"><img src="https://danielzezhengjiang.com/favicon-32x32.png?v=c167ace869f6a41a53ba76a471eab618" class="icon bookmark-icon"/>https://danielzezhengjiang.com/</div></div><img src="https://danielzezhengjiang.com/twitter-img.png" class="bookmark-image"/></a></figure><figure id="aa415446-95d1-45cc-848a-743f0597990c"><a href="https://dailyorange.com/2015/10/qa-freshman-free-line-skater-talks-alternative-transportation/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Q&amp;A: Freshman free-line skater talks alternative transportation - The Daily Orange</div><div class="bookmark-description">Freshman Daniel Jiang turns heads when going from place to place on campus. His free-line skates - two platforms, one for each foot, with no straps to secure them on his feet - provide him with an unusual method of transportation.</div></div><div class="bookmark-href"><img src="https://dailyorange.com/favicon.ico" class="icon bookmark-icon"/>https://dailyorange.com/2015/10/qa-freshman-free-line-skater-talks-alternative-transportation/</div></div><img src="https://dailyorange.com/resize/220x180/wp-content/uploads/2022/11/16235545/CourtesyofWallyGobetz.jpg" class="bookmark-image"/></a></figure><figure id="8e48105d-5117-455e-8326-32af00eaf704"><a href="https://lcmsyracuse.org/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Lutheran Campus Ministry, Syracuse</div><div class="bookmark-description">The variety of subjects taught at Success Saturday gave me, an international student, a glance of the impressive breadth of knowledge of secondary education in US. To name a few I have helped with, in no particular order: Biology, Macroeconomics, Accounting, Statistics, Algebra, Geometry, Geology, American History, US Constitution and political system, Shakespeare, Hemingway...</div></div><div class="bookmark-href"><img src="https://lcmsyracuse.org/wp-content/uploads/2019/11/3232.png" class="icon bookmark-icon"/>https://lcmsyracuse.org/</div></div><img src="https://lcmsyracuse.org/wp-content/uploads/2020/05/Screen-Shot-2020-05-01-at-8.49.03-PM.jpg" class="bookmark-image"/></a></figure><figure id="1d00edf7-a2ef-4774-8503-8343e124129f"><a href="https://skaneateleslake.org/renew-membership/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Renew Membership</div><div class="bookmark-description">Support the SLA through Amazon Smile... Every Little Bit Helps The Skaneateles Lake Association has registered with Amazon to be a recipient under their Amazon Smile Program. This program enables you to choose the Skaneateles Lake Association as the recipient of a donation from Amazon each time you shop on Amazon.</div></div><div class="bookmark-href"><img src="https://skaneateleslake.org/SLA/wp-content/uploads/2020/04/LF-favicon.png" class="icon bookmark-icon"/>https://skaneateleslake.org/renew-membership/</div></div><img src="https://skaneateleslake.org/SLA/wp-content/uploads/2015/01/lakeHeaderPier.jpg" class="bookmark-image"/></a></figure><figure id="3a2cacd5-50ce-4798-811a-f7c2a0372ce8"><a href="http://www.fiddlersgreenpark.org/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Fiddlers Green Park</div></div><div class="bookmark-href"><img src="http://www.fiddlersgreenpark.org/favicon.ico" class="icon bookmark-icon"/>http://www.fiddlersgreenpark.org/</div></div><img src="http://www.fiddlersgreenpark.org/images/indexPage/spring_cropped.jpg" class="bookmark-image"/></a></figure></li></ul></div></article></body></html>
'''