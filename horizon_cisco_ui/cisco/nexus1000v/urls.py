#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls import patterns
from django.conf.urls import url

from horizon_cisco_ui.cisco.nexus1000v import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Network Profile
    url(r'^network_profile/create$', views.CreateNetworkProfileView.as_view(),
        name='create_network_profile'),
    url(r'^network_profile/(?P<profile_id>[^/]+)/update$',
        views.UpdateNetworkProfileView.as_view(),
        name='update_network_profile'),
)
