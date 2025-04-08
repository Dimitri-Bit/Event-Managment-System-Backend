"""database seeding

Revision ID: 7ac5723bede6
Revises: ffe0fae20d21
Create Date: 2025-04-07 21:30:11.592219

"""
from typing import List, Sequence, Union

from alembic import op
import sqlalchemy as sa
from util.password_manager import PasswordManager


# revision identifiers, used by Alembic.
revision: str = '7ac5723bede6'
down_revision: Union[str, None] = 'ffe0fae20d21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
password_manager = PasswordManager()

party_image_links = [
    "https://th.bing.com/th/id/OIP.8KQ23-hfDmIAJ85fdS3E7QHaE7?rs=1&pid=ImgDetMain",
    "https://media.timeout.com/images/103926031/image.jpg",
    "https://images.startups.co.uk/wp-content/uploads/2011/04/22180804/How-to-start-a-party-and-event-planning-business.jpg",
    "https://th.bing.com/th/id/OIP.Rfv_NnBdYFGpt-WinNik7QHaFj?rs=1&pid=ImgDetMain",
    "https://images.pexels.com/photos/1047940/pexels-photo-1047940.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260",
    "https://images.pexels.com/photos/1047940/pexels-photo-1047940.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260",
    "https://th.bing.com/th/id/OIP.Hv1XLYTy0G7ibP-vwD6eWgHaE7?rs=1&pid=ImgDetMain",
    "https://cdn.pixabay.com/photo/2023/01/18/14/39/family-7727035_1280.jpg",
    "https://static.vecteezy.com/system/resources/thumbnails/024/308/218/small_2x/happy-people-with-champagne-on-christmas-party-illustration-ai-generative-free-photo.jpg",
    "https://media.textadventures.co.uk/coverart/b69281d8-93b6-4c6a-a964-441dddfe8a9d.jpg",
    "https://th.bing.com/th/id/OIP.wgvkmmL2XnbI9iuPo9gt7QHaE8?rs=1&pid=ImgDetMain",
    "https://static.vecteezy.com/system/resources/thumbnails/012/429/086/small_2x/multiethnic-group-of-casual-business-people-having-confetti-party-free-photo.JPG",
    "https://images.pexels.com/photos/2342400/pexels-photo-2342400.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://th.bing.com/th/id/R.7abe7609548919d06702ffcab85bfb81?rik=T%2bGAjbaiB2A1Gg&pid=ImgRaw&r=0",
    "https://www2.gvsu.edu/orazemm/pictures/PartyPicturesfrom200405/photos/photo21.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM182UefugnrYpe0mlBvsA4wp0bG9UYaltFg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1m1BwE8YASlmtY7-xqRH3-ecSNGZ7d4xEWg&s",
    "https://mynight.aktualno.si/wp-content/uploads/2023/11/1039896574098658.jpeg",
    "https://cdn-az.allevents.in/events4/banners/6816233777858eb626bfc4dcdc7022ef12ffec2e1b2386875c44b81afdafe400-rimg-w1200-h675-dc1d1c5a-gmir?v=1743862644",
    "https://i.redd.it/party-on-80s-edition-vintage-photos-of-parties-in-the-1980s-v0-i8pboep7474c1.jpg?width=640&format=pjpg&auto=webp&s=89dc8dda596669aa467375dec2aa49b67ac6e81d",
    "https://i.pinimg.com/736x/98/46/19/984619ae0c784b642df8525cec1ca6ae.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFcKudiAf4jwQoq7m7IE0lGFSKmekxaYzbvw&s",
    "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://cataas.com/cat",
    "https://cataas.com/cat",
    "https://cataas.com/cat"
]

party_names = [
    "Keg Stand Kingdom",
    "Toga Takedown",
    "Neon Nights",
    "Blacklight Bash",
    "Margarita Mayhem",
    "Tropical Thunder",
    "Red Cup Rendezvous",
    "Foam Frenzy",
    "Silent Disco Delight",
    "Casino Royale Night",
    "Country Chaos",
    "Luau Lockdown",
    "Masquerade Madness",
    "Pajama Jam",
    "Decades Throwdown",
    "Glow Stick Galaxy",
    "White Trash Bash",
    "Anything But Clothes",
    "ABC Party",
    "Derby Day Drunk Fest",
    "Cinco de Drinko",
    "St. Patrick's Shenanigans",
    "Halloween Hootenanny",
    "Winter Wonderland Wasted",
    "Spring Break Spree"
]

party_descriptions = [
    "Prepare for gravity-defying feats of drinking prowess. Keg stands all night!",
    "Dust off your best sheet and sandals. It's a classic toga party!",
    "Get ready to glow! We're lighting up the night with neon everything.",
    "Wear white or bright colors to shine under the blacklights. Prepare for the unexpected!",
    "Salt rims and good times guaranteed. Tequila-fueled fun all night long.",
    "Escape to a tropical paradise (sort of). Think Hawaiian shirts and fruity drinks.",
    "The quintessential college party. Red cups, good music, and even better company.",
    "Dive into a sea of suds! Get ready to get wet and wild.",
    "Put on your headphones and dance to your own beat. Multiple DJs, your choice of music.",
    "Dress to impress in your finest attire. High stakes and maybe some low ones too.",
    "Boots, buckles, and beer. Get ready for some down-home fun and maybe a little line dancing.",
    "Grass skirts, leis, and island vibes. Let's hula the night away.",
    "Mystery and intrigue abound. Don a mask and become someone else for the night.",
    "Comfort is key! Roll out of bed and into the party in your favorite PJs.",
    "Travel through time with the best hits from different decades. Dress your favorite era!",
    "Light up the night with an array of glow sticks. Dance until you're a human light show.",
    "Embrace your inner redneck. Flannel, trucks, and maybe some questionable decisions.",
    "Get creative (or not so much). Wear anything... as long as it's not clothes.",
    "Anything But Cups! Get inventive with how you'll be enjoying your beverages.",
    "Big hats and mint juleps. Celebrate the races with style (and maybe a stumble or two).",
    "Tacos, tequila, and good times. Celebrate Cinco de Mayo the right way.",
    "Wear your green and get ready for some Irish cheer (and maybe a bit too much Guinness).",
    "Dress spooky and get ready for a frightfully good time. Costumes are a must!",
    "Bundle up and get ready for a chilly celebration. Think winter-themed drinks and decorations.",
    "Let loose and soak up the (almost) summer vibes. Beach attire encouraged!"
]

date_list = [
    {'start_date': '2025-04-10', 'end_date': '2025-04-12'},
    {'start_date': '2025-05-01', 'end_date': '2025-05-03'},
    {'start_date': '2025-06-15', 'end_date': '2025-06-16'},
    {'start_date': '2025-07-20', 'end_date': '2025-07-23'},
    {'start_date': '2025-08-05', 'end_date': '2025-08-06'},
    {'start_date': '2025-09-11', 'end_date': '2025-09-14'},
    {'start_date': '2025-10-22', 'end_date': '2025-10-24'},
    {'start_date': '2025-11-01', 'end_date': '2025-11-02'},
    {'start_date': '2025-12-18', 'end_date': '2025-12-20'},
    {'start_date': '2026-01-03', 'end_date': '2026-01-05'},
    {'start_date': '2026-02-14', 'end_date': '2026-02-15'},
    {'start_date': '2026-03-29', 'end_date': '2026-04-01'},
    {'start_date': '2026-04-08', 'end_date': '2026-04-09'},
    {'start_date': '2026-05-19', 'end_date': '2026-05-21'},
    {'start_date': '2026-06-25', 'end_date': '2026-06-27'},
    {'start_date': '2026-07-10', 'end_date': '2026-07-11'},
    {'start_date': '2026-08-22', 'end_date': '2026-08-25'},
    {'start_date': '2026-09-01', 'end_date': '2026-09-03'},
    {'start_date': '2026-10-16', 'end_date': '2026-10-17'},
    {'start_date': '2026-11-27', 'end_date': '2026-11-29'},
    {'start_date': '2026-12-05', 'end_date': '2026-12-06'},
    {'start_date': '2027-01-19', 'end_date': '2027-01-21'},
    {'start_date': '2027-02-23', 'end_date': '2027-02-24'},
    {'start_date': '2027-03-08', 'end_date': '2027-03-10'},
    {'start_date': '2027-04-15', 'end_date': '2027-04-17'}
]

country_town_list = [
    {'country': 'Montenegro', 'town': 'Podgorica'},
    {'country': 'Montenegro', 'town': 'Nikšić'},
    {'country': 'Montenegro', 'town': 'Cetinje'},
    {'country': 'Montenegro', 'town': 'Budva'},
    {'country': 'Montenegro', 'town': 'Herceg Novi'},
    {'country': 'Serbia', 'town': 'Belgrade'},
    {'country': 'Serbia', 'town': 'Novi Sad'},
    {'country': 'Serbia', 'town': 'Niš'},
    {'country': 'Albania', 'town': 'Tirana'},
    {'country': 'Albania', 'town': 'Durrës'},
    {'country': 'Bosnia and Herzegovina', 'town': 'Sarajevo'},
    {'country': 'Bosnia and Herzegovina', 'town': 'Mostar'},
    {'country': 'Croatia', 'town': 'Zagreb'},
    {'country': 'Croatia', 'town': 'Split'},
    {'country': 'North Macedonia', 'town': 'Skopje'},
    {'country': 'Greece', 'town': 'Athens'},
    {'country': 'Italy', 'town': 'Rome'},
    {'country': 'Austria', 'town': 'Vienna'},
    {'country': 'Hungary', 'town': 'Budapest'},
    {'country': 'Bulgaria', 'town': 'Sofia'},
    {'country': 'Romania', 'town': 'Bucharest'},
    {'country': 'Slovenia', 'town': 'Ljubljana'},
    {'country': 'Kosovo', 'town': 'Pristina'},
    {'country': 'Switzerland', 'town': 'Zurich'},
    {'country': 'Germany', 'town': 'Berlin'}
]

party_types = [
    "Rave",
    "Techno",
    "House",
    "Trance",
    "Hip-Hop",
    "Rock",
    "Jazz",
    "Karaoke",
    "Disco",
    "Funk",
    "Soul",
    "Pop",
    "Electronic",
    "Dance",
    "Glow",
    "Masquerade",
    "Themed",
    "Yugo Rock",
    "Rave",
    "Techno",
    "House",
    "Trance",
    "Hip-Hop",
    "Rock",
    "Jazz"
]

def generate_user_list() -> List[dict]:
    users = []

    for i in range(2, 25):
        email = f"user{i}@user.com"
        username = f"username{i}"
        password = password_manager.get_password_hash(f"userpassword{i}")
        user = {"email": email, "username": username, "password": password}
        users.append(user)
    return users

def generate_role_user_list() -> List[dict]:
    role_users = []
    for i in range(2, 25):
        role_id = 1
        if (i >= 20): # Make some admins for the graphs
            role_id = 2
        user_id = i
        role_user = {"role_id": role_id, "user_id": user_id}
        role_users.append(role_user)
    return role_users

def generate_parties_list() -> List[dict]:
    parties = []
    for i in range (2, 25):
        party = {
            "id": (i-1),
            "name_party": party_names[i],
            "url_image_full": party_image_links[i],
            "name_organizer": f"username{i}",
            "date_start": date_list[i]["start_date"],
            "date_end": date_list[i]["end_date"],
            "name_town": country_town_list[i]["town"],
            "name_country": country_town_list[i]["country"],
            "name_type": party_types[i],
            "text_entry_fee": "0",
            "text_more": party_descriptions[i],
            "url_organizer": "",
            "url_party": "",
            "user_id": i
        }
        parties.append(party)

    return parties

def seed_users():
    op.bulk_insert(
        sa.table("users", sa.Column("email"), sa.Column("username"), sa.Column("password")),
        generate_user_list()
    )

def seed_role_user():
    op.bulk_insert(
        sa.table("role_user", sa.Column("role_id"), sa.Column("user_id")),
        generate_role_user_list()
    )

def seed_parties():
    op.bulk_insert(
        sa.table("parties",
            sa.Column("id"),
            sa.Column("name_party"),
            sa.Column("url_image_full"),
            sa.Column("name_organizer"),
            sa.Column("date_start"),
            sa.Column("date_end"),
            sa.Column("name_town"),
            sa.Column("name_country"),
            sa.Column("name_type"),
            sa.Column("text_entry_fee"),
            sa.Column("text_more"),
            sa.Column("url_organizer"),
            sa.Column("url_party"),
            sa.Column("user_id")
        ),
        generate_parties_list()
    )

def upgrade() -> None:
    """Upgrade schema."""
    seed_users()
    seed_role_user()
    seed_parties()
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
