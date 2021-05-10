from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(_(r'^cart/'), include(('cart.urls', 'cart'), namespace='cart')),
    url(_(r'^orders/'), include(('orders.urls', 'orders'), namespace='orders')),
    url(_(r'^coupons/'), include(('coupons.urls', 'coupons'), namespace='coupons')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
