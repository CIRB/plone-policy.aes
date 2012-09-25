from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicyAes(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.aes
        xmlconfig.file('configure.zcml',
                       policy.aes,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.aes:default')

POLICY_AES_FIXTURE = PolicyAes()
POLICY_AES_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_AES_FIXTURE, ),
                       name="PolicyAes:Integration")