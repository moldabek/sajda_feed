from django.db import models


class Card(models.Model):
    CARD_TYPE = (
        ('QURAN_AYAH', 'Quran Ayah'),
        ('HADITH', 'Hadith'),
        ('PICTURE', 'Picture'),
        ('DHIKR', 'Dhikr'),
        ('YOUTUBE', 'YouTube'),
    )

    REPEAT_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('custom', 'Custom'),
    )

    card_type = models.CharField(max_length=50, choices=CARD_TYPE)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(verbose_name='Content of the card (e.g., Ayah text, Hadith text, Dhikr title)')
    additional_info = models.TextField(
        blank=True,
        null=True,
        verbose_name='Additional information related to the card (e.g., Surah title, Name of Narrator)'
    )
    arabic_text = models.TextField(blank=True, null=True)
    content_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='URL of the content (e.g., YouTube URL, Picture URL)'
    )
    picture = models.ImageField(upload_to='cards/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    repeat = models.CharField(max_length=10, choices=REPEAT_CHOICES, default='daily')
    repeat_days = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    play_in_app = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def add_interaction(self, interaction_type: str, user) -> None:
        if interaction_type in ('like', 'hide'):
            interactions = UserCardInteraction.objects.filter(
                card=self,
                user=user,
                interaction_type=interaction_type
            )
            if interactions.exists():
                interactions.delete()
                return
        interaction = UserCardInteraction.objects.create(
            card=self,
            user=user,
            interaction_type=interaction_type
        )
        interaction.save()

    def set_user_interactions(self, user) -> None:
        liked = UserCardInteraction.objects.filter(card=self, user=user, interaction_type='like').exists()
        dhikrs_count = UserCardInteraction.objects.filter(card=self, user=user, interaction_type='dhikr').count()
        self.liked = liked
        self.dhikrs_count = dhikrs_count

    @property
    def like_count(self):
        return UserCardInteraction.objects.filter(card=self, interaction_type='like').count()

    def card_hidden(self, user):
        return UserCardInteraction.objects.filter(card=self, user=user, interaction_type='hide').exists()


class UserCardInteraction(models.Model):
    INTERACTION_TYPE = (
        ('like', 'Like'),
        ('hide', 'Hide'),
        ('dhikr', 'Dhikr'),
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Взаимодействие пользователя с карточкой'
        verbose_name_plural = 'Взаимодействия пользователей с карточками'
