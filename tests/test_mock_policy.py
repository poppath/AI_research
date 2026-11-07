"""Illustrative pure mock: no tool/credentials/production enforcement."""
import unittest


def mock_decide(action, restricted=False, status_unknown=False, rights=False,
                permission=False, consent=False, approval_matches=False, within_cap=False):
    if restricted:
        return 'REJECT'
    if status_unknown:
        return 'HOLD'
    if action == 'draft':
        return 'DRAFT'
    if action not in ('publish', 'spend'):
        return 'HOLD'
    if not (rights and permission and consent and approval_matches):
        return 'HOLD'
    if action == 'spend' and not within_cap:
        return 'HOLD'
    return 'ELIGIBLE_FOR_EXTERNAL_GATE'  # Not permission to execute.


class MockPolicyTest(unittest.TestCase):
    def test_draft_and_restricted(self):
        self.assertEqual(mock_decide('draft'), 'DRAFT')
        self.assertEqual(mock_decide('draft', restricted=True), 'REJECT')

    def test_publish_fails_closed(self):
        checks = dict(rights=True, permission=True, consent=True, approval_matches=True)
        for key in checks:
            missing = dict(checks, **{key: False})
            self.assertEqual(mock_decide('publish', **missing), 'HOLD', key)
        self.assertEqual(mock_decide('publish', **checks), 'ELIGIBLE_FOR_EXTERNAL_GATE')
        self.assertEqual(mock_decide('publish', status_unknown=True, **checks), 'HOLD')

    def test_spend_needs_cap_and_matching_approval(self):
        checks = dict(rights=True, permission=True, consent=True, approval_matches=True)
        self.assertEqual(mock_decide('spend', **checks), 'HOLD')
        self.assertEqual(mock_decide('spend', within_cap=True, **checks), 'ELIGIBLE_FOR_EXTERNAL_GATE')
        self.assertEqual(mock_decide('unexpected_action', within_cap=True, **checks), 'HOLD')


if __name__ == '__main__':
    unittest.main()
