import json
import html


def safe_text(value):
    if value is None:
        return ""

    return html.escape(str(value))


def generate_skills(skills):
    if not skills:
        return "<p>No skills provided.</p>"

    result = ""

    for skill in skills:
        result += f"""
        <span class="skill">{safe_text(skill)}</span>
        """

    return result


def generate_education(education):
    if not education:
        return "<p>No education information provided.</p>"

    result = ""

    for item in education:

        if isinstance(item, dict):

            degree = item.get(
                "degree",
                item.get("title", "")
            )

            institution = item.get(
                "institution",
                ""
            )

            year = item.get(
                "year",
                ""
            )

            result += f"""
            <div class="card">
                <h3>{safe_text(degree)}</h3>
                <p>{safe_text(institution)}</p>
                <span>{safe_text(year)}</span>
            </div>
            """

        else:

            result += f"""
            <div class="card">
                <p>{safe_text(item)}</p>
            </div>
            """

    return result


def generate_projects(projects):
    if not projects:
        return "<p>No projects provided.</p>"

    result = ""

    for project in projects:

        if isinstance(project, dict):

            title = project.get(
                "title",
                project.get("name", "Project")
            )

            description = project.get(
                "description",
                project.get("details", "")
            )

            technologies = project.get(
                "technologies",
                project.get("tech_stack", [])
            )

            if isinstance(technologies, list):
                technologies = ", ".join(
                    safe_text(item)
                    for item in technologies
                )

            result += f"""
            <div class="card project-card">

                <h3>{safe_text(title)}</h3>

                <p>{safe_text(description)}</p>

                <small>
                    {safe_text(technologies)}
                </small>

            </div>
            """

        else:

            result += f"""
            <div class="card project-card">
                <p>{safe_text(project)}</p>
            </div>
            """

    return result


def generate_experience(experience):
    if not experience:
        return "<p>No experience information provided.</p>"

    result = ""

    for item in experience:

        if isinstance(item, dict):

            role = item.get(
                "role",
                item.get("position", "")
            )

            company = item.get(
                "company",
                ""
            )

            duration = item.get(
                "duration",
                ""
            )

            description = item.get(
                "description",
                ""
            )

            result += f"""
            <div class="card">

                <h3>{safe_text(role)}</h3>

                <h4>{safe_text(company)}</h4>

                <span>{safe_text(duration)}</span>

                <p>{safe_text(description)}</p>

            </div>
            """

        else:

            result += f"""
            <div class="card">
                <p>{safe_text(item)}</p>
            </div>
            """

    return result


def generate_achievements(achievements):
    if not achievements:
        return "<p>No achievements provided.</p>"

    result = ""

    for achievement in achievements:

        result += f"""
        <li>{safe_text(achievement)}</li>
        """

    return result


def generate_contact(contact):

    if not isinstance(contact, dict):
        return ""

    email = safe_text(
        contact.get("email", "")
    )

    phone = safe_text(
        contact.get("phone", "")
    )

    result = ""

    if email:
        result += f"""
        <p>
            Email:
            <a href="mailto:{email}">
                {email}
            </a>
        </p>
        """

    if phone:
        result += f"""
        <p>
            Phone: {phone}
        </p>
        """

    return result


def generate_links(links):

    if not isinstance(links, dict):
        return ""

    linkedin = safe_text(
        links.get("linkedin", "")
    )

    github = safe_text(
        links.get("github", "")
    )

    result = ""

    if linkedin:
        result += f"""
        <a href="{linkedin}"
           target="_blank">
           LinkedIn
        </a>
        """

    if github:
        result += f"""
        <a href="{github}"
           target="_blank">
           GitHub
        </a>
        """

    return result


def generate_portfolio(portfolio_data):

    try:

        with open(
    "templates/portfolio.html",
    "r",
    encoding="utf-8"
    ) as file:

            template = file.read()

        name = safe_text(
            portfolio_data.get("name", "")
        )

        headline = safe_text(
            portfolio_data.get("headline", "")
        )

        summary = safe_text(
            portfolio_data.get(
                "professional_summary",
                ""
            )
        )

        skills = generate_skills(
            portfolio_data.get("skills", [])
        )

        education = generate_education(
            portfolio_data.get("education", [])
        )

        experience = generate_experience(
            portfolio_data.get("experience", [])
        )

        projects = generate_projects(
            portfolio_data.get("projects", [])
        )

        achievements = generate_achievements(
            portfolio_data.get("achievements", [])
        )

        contact = generate_contact(
            portfolio_data.get("contact", {})
        )

        links = generate_links(
            portfolio_data.get("links", {})
        )

        template = template.replace(
            "{{NAME}}",
            name
        )

        template = template.replace(
            "{{HEADLINE}}",
            headline
        )

        template = template.replace(
            "{{SUMMARY}}",
            summary
        )

        template = template.replace(
            "{{SKILLS}}",
            skills
        )

        template = template.replace(
            "{{EDUCATION}}",
            education
        )

        template = template.replace(
            "{{EXPERIENCE}}",
            experience
        )

        template = template.replace(
            "{{PROJECTS}}",
            projects
        )

        template = template.replace(
            "{{ACHIEVEMENTS}}",
            achievements
        )

        template = template.replace(
            "{{CONTACT}}",
            contact
        )

        template = template.replace(
            "{{LINKS}}",
            links
        )

        with open(
            "portfolio.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(template)

        print(
            "Portfolio generated successfully!"
        )

        return "portfolio.html"

    except FileNotFoundError:

        print(
            "ERROR: template.html not found."
        )

        return None

    except Exception as error:

        print(
            "Portfolio generation error:"
        )

        print(error)

        return None