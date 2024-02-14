import attr


@attr.s(auto_attribs=True)
class QuranAyah:
    ayah: str
    surah: str
    ayah_number: str
    surah_name: str
    surah_number: str
    arabic_text: str


@attr.s(auto_attribs=True)
class Hadith:
    name_of_narrator: str
    title: str
    hadith: str
    source: str
    arabic_text: str


if __name__ == '__main__':
    q = QuranAyah(
        ayah="In the name of Allah, the Entirely Merciful, the Especially Merciful.",
        surah="Al-Fatiha",
        ayah_number="1",
        surah_name="The Opening",
        surah_number="1",
        arabic_text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
    )
    assert q.ayah == "In the name of Allah, the Entirely Merciful, the Especially Merciful."
    assert q.surah == "Al-Fatiha"
    assert q.ayah_number == "1"
    assert q.surah_name == "The Opening"
    assert q.surah_number == "1"
    assert q.arabic_text == "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"

    h = Hadith(
        name_of_narrator="Abu Huraira",
        hadith="The Prophet (ﷺ) said, \"The example of a believer is like a fresh tender plant; from whatever direction the wind comes, it bends it, but when the wind becomes quiet, it becomes straight again. Similarly, a believer is afflicted with calamities (but he remains patient till Allah removes his difficulties.) And an impious wicked person is like a pine tree which keeps hard and straight till Allah cuts (breaks) it down when He wishes.\"",
        source="Sahih al-Bukhari 5645",
        arabic_text="حَدَّثَنَا مُحَمَّدُ بْنُ الْمُثَنَّى، حَدَّثَنَا اللَّيْثُ، عَنْ يَزِيدَ بْنِ أَبِي حَبِيبٍ، عَنْ عُرْوَةَ، عَنْ عَائِشَةَ ـ رضى الله عنها ـ قَالَتْ قَالَ رَسُولُ اللَّهِ صلى الله عليه وسلم ‏ \"‏ مَثَلُ الْمُؤْمِنِ كَمَثَلِ النَّبَاتِ الطَّيِّبِ، لَا تَثْبُتُهُ رِيحٌ مِنْ حَيْثُ شَاءَتْ، وَمَثَلُ الْفَاجِرِ كَالسَّنْبَلَةِ الرَّيَّانِ، لَا تَنْثُرُهَا رِيحٌ حَتَّى تُقَطِّعَهَا\"‏‏",
        title="The example of a believer"
    )
