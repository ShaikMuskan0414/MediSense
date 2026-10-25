from flask import Flask, render_template, jsonify, request
from database import get_hospital, get_hospitals

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.get("/api/hospitals")
def hospitals():
    specialty = request.args.get("specialty", "").strip()
    rows = get_hospitals(specialty)
    return jsonify(rows)


@app.get("/api/hospitals/<int:hospital_id>/insurance")
def hospital_insurance(hospital_id):
    hospital = get_hospital(hospital_id)

    if not hospital:
        return jsonify({"error": "Hospital not found"}), 404

    def split_values(value):
        if not value:
            return []

        import re
        parts = re.split(r"[,;|\n]+", str(value))
        return [p.strip() for p in parts if p.strip()]

    result = []

    for name in split_values(hospital.get("private_insurance_companies")):
        result.append({
            "name": name,
            "type": "Private Insurance"
        })

    for name in split_values(hospital.get("tpa_partners")):
        result.append({
            "name": name,
            "type": "TPA Partner"
        })

    for name in split_values(hospital.get("government_schemes")):
        result.append({
            "name": name,
            "type": "Government Scheme"
        })

    # Remove duplicate insurance names
    seen = set()
    unique = []

    for item in result:
        key = item["name"].casefold()

        if key not in seen:
            seen.add(key)
            unique.append(item)

    return jsonify(unique)


@app.get("/api/specialties")
def specialties():
    rows = get_hospitals()

    specialty_set = set()

    import re

    for row in rows:
        value = row.get("health_specialties")

        if not value:
            continue

        parts = re.split(r"[,;|\n]+", str(value))

        for part in parts:
            part = part.strip()

            if part:
                specialty_set.add(part)

    return jsonify(sorted(specialty_set))


if __name__ == "__main__":
    app.run(debug=True)