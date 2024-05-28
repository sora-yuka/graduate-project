from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("./apps/account/template/email.html")

full_link = "link to verify"
output = template.render(full_link=full_link)
print(output)