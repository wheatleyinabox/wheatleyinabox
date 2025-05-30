from pathLib import Path

template = Path("assets/hello.svg").read_text()

for theme in ["light", "dark"]:
  css = Path(f"assets/{theme}-hello.css").read_text()
  output = template.replace("/* THEME_CSS */", css)
  Path(f"output/{theme}.svg").write_text(ouput)
